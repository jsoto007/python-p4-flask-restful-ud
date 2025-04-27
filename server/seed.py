#!/usr/bin/env python3

from faker import Faker

from app import app
from models import db, Newsletter

print("seeding 🌱🌱🌱")

with app.app_context():
    
    fake = Faker()

    Newsletter.query.delete()

    newsletters = []
    for i in range(50):
        newsletter = Newsletter(
            title = fake.text(max_nb_chars=20),
            body = fake.paragraph(nb_sentences=5),
        )
        newsletters.append(newsletter)

    db.session.add_all(newsletters)
    db.session.commit()

print("Done Seeding 🪴🪴🪴")