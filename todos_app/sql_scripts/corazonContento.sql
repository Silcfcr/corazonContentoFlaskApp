-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema corazon_lleno_2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema corazon_lleno_2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `corazon_lleno_2` DEFAULT CHARACTER SET utf8 ;
USE `corazon_lleno_2` ;

-- -----------------------------------------------------
-- Table `corazon_lleno_2`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `corazon_lleno_2`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `user_type` VARCHAR(45) NULL DEFAULT NULL,
  `type` VARCHAR(45) NULL DEFAULT NULL,
  `population` INT NULL DEFAULT NULL,
  `state` VARCHAR(45) NULL DEFAULT NULL,
  `city` VARCHAR(45) NULL DEFAULT NULL,
  `address` VARCHAR(45) NULL DEFAULT NULL,
  `contact_first_name` VARCHAR(45) NULL DEFAULT NULL,
  `contact_last_name` VARCHAR(45) NULL DEFAULT NULL,
  `contact_phone` VARCHAR(45) NULL DEFAULT NULL,
  `contact_email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `corazon_lleno_2`.`donations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `corazon_lleno_2`.`donations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NULL DEFAULT NULL,
  `transport` VARCHAR(45) NULL DEFAULT NULL,
  `portions` INT NULL DEFAULT NULL,
  `expiration` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `status` VARCHAR(45) NULL DEFAULT NULL,
  `donator_id` INT NOT NULL,
  `receiver_id` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_donations_users1_idx` (`donator_id` ASC) VISIBLE,
  CONSTRAINT `fk_donations_users1`
    FOREIGN KEY (`donator_id`)
    REFERENCES `corazon_lleno_2`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
