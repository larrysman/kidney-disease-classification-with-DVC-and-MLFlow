# MODEL TRAINING MODULE - THE TRANSFER TRAINING FROM BASE MODEL


from pathlib import Path
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
tf.config.run_functions_eagerly(True)
from src.Kidney_classifier.entity.config_entity import TrainingModelConfig



class ModelTraining:
    def __init__(self, config: TrainingModelConfig):
        self.config = config

    
    def get_updated_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

        # YOU NEED TO ALWAYS RECOMPILE YOUR MODEL FOR TRANSFER LEARNING (wHEN YOU LOAD A KERAS MODEL ALWAYS RE-COMPILE)
        optimizer = Adam()
        self.model.compile(
            optimizer=optimizer,
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )

    
    def training_validation_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.10
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        validation_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.validation_generator = validation_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_augmentation:
            training_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            training_datagenerator = validation_datagenerator

        self.training_generator = training_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def model_training(self):
        self.steps_per_epoch = self.training_generator.samples // self.training_generator.batch_size
        self.validation_steps = self.validation_generator.samples // self.validation_generator.batch_size

        self.model.fit(
            self.training_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.validation_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

