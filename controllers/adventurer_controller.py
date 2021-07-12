from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.adventurer import Adventurer
import repositories.adventurer_repository as adventurer_repository

adventurers_blueprint = Blueprint("adventurers", __name__)