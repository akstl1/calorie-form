from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Calorie
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # note = request.form.get('note')
        date = datetime.strptime(request.form.get('date'),'%Y-%m-%d')
        breakfast_green = request.form.get('breakfast_green')
        print(breakfast_green)
        lunch_green = request.form.get('lunch_green')
        dinner_green = request.form.get('dinner_green')
        snack_green = request.form.get('snack_green')
        breakfast_yellow = request.form.get('breakfast_yellow')
        lunch_yellow = request.form.get('lunch_yellow')
        dinner_yellow = request.form.get('dinner_yellow')
        snack_yellow = request.form.get('snack_yellow')
        breakfast_red = request.form.get('breakfast_red')
        lunch_red = request.form.get('lunch_red')
        dinner_red = request.form.get('dinner_red')
        snack_red = request.form.get('snack_red')
        if snack_red=='1000000':
            pass
            # flash('Date can\'t be in the future!', category='error')
        else:
            new_calories = Calorie(
                                    date=date,
                                   breakfast_green=breakfast_green,
                                   lunch_green=lunch_green,
                                   dinner_green=dinner_green,
                                   snack_green=snack_green,
                                   breakfast_yellow=breakfast_yellow,
                                   lunch_yellow=lunch_yellow,
                                   dinner_yellow=dinner_yellow,
                                   snack_yellow=snack_yellow,
                                   breakfast_red=breakfast_red,
                                   lunch_red=lunch_red,
                                   dinner_red=dinner_red,
                                   snack_red=snack_red,
                                   user_id=current_user.id)
            db.session.add(new_calories)
            print(new_calories.dinner_red)
            db.session.commit()
            flash('Calories added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-calories', methods=['POST'])
def delete_calories():
    calorie = json.loads(request.data)
    calorieId = calorie['calorieId']
    calorie = Calorie.query.get(calorieId)
    if calorie:
        if calorie.user_id == current_user.id:
            db.session.delete(calorie)
            db.session.commit()

    return jsonify({})
