
import pygame
import sys
import os
import random
from pygame.locals import *

sounds = {}  # create empty dictionary of sounds


def initSoundManager():
    pygame.mixer.init()
    sounds["fire"] = pygame.mixer.Sound("Sonidos/FIRE.WAV")
    sounds["explode1"] = pygame.mixer.Sound("Sonidos/EXPLODE1.WAV")
    sounds["explode2"] = pygame.mixer.Sound("Sonidos/EXPLODE2.WAV")
    sounds["explode3"] = pygame.mixer.Sound("Sonidos/EXPLODE3.WAV")
    sounds["lsaucer"] = pygame.mixer.Sound("Sonidos/LSAUCER.WAV")
    sounds["ssaucer"] = pygame.mixer.Sound("Sonidos/SSAUCER.WAV")
    sounds["thrust"] = pygame.mixer.Sound("Sonidos/THRUST.WAV")
    sounds["sfire"] = pygame.mixer.Sound("Sonidos/SFIRE.WAV")
    sounds["extralife"] = pygame.mixer.Sound("Sonidos/LIFE.WAV")


def playSound(soundName):
    channel = sounds[soundName].play()


def playSoundContinuous(soundName):
    channel = sounds[soundName].play(-1)


def stopSound(soundName):
    channel = sounds[soundName].stop()
