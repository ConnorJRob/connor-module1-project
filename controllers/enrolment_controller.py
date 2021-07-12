from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.enrolment import Enrolment
import repositories.enrolment_repository as enrolment_repository

enrolments_blueprint = Blueprint("enrolments", __name__)