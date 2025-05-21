from flask import Flask, render_template, request, redirect, url_for, flash
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # DON'T CHANGE THIS !!!

app = Flask(__name__)
app.secret_key = 'kari_kulu_hire_cars_secret_key'

# Vehicle data
vehicles = [
    {
        'id': 1,
        'name': 'Toyota Land Cruiser 5-Door',
        'type': 'SUV',
        'image': 'toyota landcruzer 5door.jpg',
        'passengers': 7,
        'fuel': 'Diesel',
        'transmission': 'Automatic',
        'drive': '4WD',
        'price': 1000,
        'description': 'Rugged and reliable 4WD vehicle perfect for all terrains. Spacious interior with ample luggage space.',
        'features': ['Air Conditioning', 'Power Steering', 'Electric Windows', 'Central Locking', 'CD Player', 'ABS Brakes'],
        'specs': {
            'Engine': '4.5L V8 Diesel',
            'Power': '202 kW',
            'Torque': '650 Nm',
            'Fuel Capacity': '138 L',
            'Fuel Consumption': '10.7 L/100km',
            'Ground Clearance': '230 mm'
        },
        'popular': True
    },
    {
        'id': 2,
        'name': 'Toyota Hilux 7th Element',
        'type': 'Pickup',
        'image': 'Toyota Hilux 7th element.jpg',
        'passengers': 5,
        'fuel': 'Diesel',
        'transmission': 'Automatic',
        'drive': '4WD',
        'price': 850,
        'description': 'Versatile pickup truck with excellent off-road capabilities. Perfect for both work and adventure.',
        'features': ['Air Conditioning', 'Power Steering', 'Electric Windows', 'Central Locking', 'Bluetooth', 'ABS Brakes'],
        'specs': {
            'Engine': '2.8L Turbo Diesel',
            'Power': '150 kW',
            'Torque': '500 Nm',
            'Fuel Capacity': '80 L',
            'Fuel Consumption': '8.0 L/100km',
            'Payload': '1000 kg'
        },
        'popular': False
    },
    {
        'id': 3,
        'name': 'Toyota Coaster Bus',
        'type': 'Bus',
        'image': 'toyota Coster Bus.jpg',
        'passengers': 22,
        'fuel': 'Diesel',
        'transmission': 'Manual',
        'drive': '2WD',
        'price': 1200,
        'description': 'Large capacity bus perfect for group transportation, tours, and events. Comfortable seating with ample luggage space.',
        'features': ['Air Conditioning', 'Power Steering', 'PA System', 'Luggage Rack', 'Comfortable Seating', 'ABS Brakes'],
        'specs': {
            'Engine': '4.0L Diesel',
            'Power': '100 kW',
            'Torque': '300 Nm',
            'Fuel Capacity': '95 L',
            'Fuel Consumption': '12.0 L/100km',
            'Length': '7.0 m'
        },
        'popular': True
    },
    {
        'id': 4,
        'name': 'Nissan Urvan Bus',
        'type': 'Bus',
        'image': 'Nissan Urvan Bus.jpg',
        'passengers': 16,
        'fuel': 'Diesel',
        'transmission': 'Manual',
        'drive': '2WD',
        'price': 850,
        'description': 'Comfortable 16-seater van perfect for group transportation. Ideal for airport transfers, tours, and corporate events.',
        'features': ['Air Conditioning', 'Power Steering', 'Electric Windows', 'Central Locking', 'CD Player', 'ABS Brakes'],
        'specs': {
            'Engine': '2.5L Diesel',
            'Power': '95 kW',
            'Torque': '356 Nm',
            'Fuel Capacity': '65 L',
            'Fuel Consumption': '9.5 L/100km',
            'Length': '5.2 m'
        },
        'popular': False
    },
    {
        'id': 5,
        'name': 'Toyota Rush',
        'type': 'SUV',
        'image': 'Toyota Rush.jpg',
        'passengers': 5,
        'fuel': 'Petrol',
        'transmission': 'Automatic',
        'drive': '2WD',
        'price': 550,
        'description': 'Compact SUV with excellent fuel efficiency. Perfect for city driving and short trips.',
        'features': ['Air Conditioning', 'Power Steering', 'Electric Windows', 'Central Locking', 'Bluetooth', 'ABS Brakes'],
        'specs': {
            'Engine': '1.5L Petrol',
            'Power': '77 kW',
            'Torque': '136 Nm',
            'Fuel Capacity': '45 L',
            'Fuel Consumption': '6.6 L/100km',
            'Ground Clearance': '200 mm'
        },
        'popular': False
    },
    {
        'id': 6,
        'name': 'Toyota Land Cruiser Single Cab',
        'type': 'Pickup',
        'image': 'toyota landcruzer single cab.jpg',
        'passengers': 3,
        'fuel': 'Diesel',
        'transmission': 'Manual',
        'drive': '4WD',
        'price': 1000,
        'description': 'Rugged single cab pickup with excellent load capacity. Perfect for work sites and heavy-duty tasks.',
        'features': ['Air Conditioning', 'Power Steering', 'Heavy Duty Suspension', 'Tow Bar', 'Bull Bar', 'Snorkel'],
        'specs': {
            'Engine': '4.5L V8 Diesel',
            'Power': '151 kW',
            'Torque': '430 Nm',
            'Fuel Capacity': '130 L',
            'Fuel Consumption': '11.2 L/100km',
            'Payload': '1200 kg'
        },
        'popular': False
    },
    {
        'id': 7,
        'name': 'Toyota Land Cruiser 10-Seater',
        'type': 'SUV',
        'image': 'Toyota landcruzer 10 seater.jpg',
        'passengers': 10,
        'fuel': 'Diesel',
        'transmission': 'Manual',
        'drive': '4WD',
        'price': 1000,
        'description': 'Spacious 10-seater 4WD vehicle perfect for large groups. Excellent for off-road adventures and tours.',
        'features': ['Air Conditioning', 'Power Steering', 'Electric Windows', 'Central Locking', 'CD Player', 'ABS Brakes'],
        'specs': {
            'Engine': '4.2L Diesel',
            'Power': '129 kW',
            'Torque': '430 Nm',
            'Fuel Capacity': '180 L',
            'Fuel Consumption': '12.5 L/100km',
            'Ground Clearance': '235 mm'
        },
        'popular': False
    },
    {
        'id': 8,
        'name': 'Toyota Land Cruiser 4-Door',
        'type': 'SUV',
        'image': 'toyota land cruzer 4door.jpg',
        'passengers': 5,
        'fuel': 'Diesel',
        'transmission': 'Manual',
        'drive': '4WD',
        'price': 1000,
        'description': 'Classic 4-door Land Cruiser with excellent off-road capabilities. Perfect for rugged terrain and adventures.',
        'features': ['Air Conditioning', 'Power Steering', 'Electric Windows', 'Central Locking', 'CD Player', 'ABS Brakes'],
        'specs': {
            'Engine': '4.2L Diesel',
            'Power': '129 kW',
            'Torque': '430 Nm',
            'Fuel Capacity': '90 L',
            'Fuel Consumption': '11.5 L/100km',
            'Ground Clearance': '230 mm'
        },
        'popular': False
    },
    {
        'id': 9,
        'name': 'Ford Ranger StormTrack',
        'type': 'Pickup',
        'image': 'Fordranger StormTrack.jpg',
        'passengers': 5,
        'fuel': 'Diesel',
        'transmission': 'Automatic',
        'drive': '4WD',
        'price': 850,
        'description': 'Premium pickup truck with advanced features and excellent performance. Perfect for both work and leisure.',
        'features': ['Air Conditioning', 'Power Steering', 'Electric Windows', 'Central Locking', 'Bluetooth', 'ABS Brakes'],
        'specs': {
            'Engine': '2.0L Bi-Turbo Diesel',
            'Power': '157 kW',
            'Torque': '500 Nm',
            'Fuel Capacity': '80 L',
            'Fuel Consumption': '7.4 L/100km',
            'Payload': '950 kg'
        },
        'popular': False
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vehicles')
def vehicle_list():
    return render_template('vehicles.html')

@app.route('/vehicle/<int:id>')
def vehicle_detail(id):
    vehicle = next((v for v in vehicles if v['id'] == id), None)
    if vehicle:
        related_vehicles = [v for v in vehicles if v['type'] == vehicle['type'] and v['id'] != id][:3]
        return render_template('vehicle_detail.html', vehicle=vehicle, related_vehicles=related_vehicles)
    return redirect(url_for('vehicle_list'))

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Process booking form
        booking_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'vehicle_id': int(request.form.get('vehicle_id')),
            'pickup_date': request.form.get('pickup_date'),
            'return_date': request.form.get('return_date'),
            'pickup_location': request.form.get('pickup_location'),
            'return_location': request.form.get('return_location'),
            'additional_info': request.form.get('additional_info')
        }
        
        # In a real application, this would be saved to a database
        # For now, we'll just redirect to a confirmation page
        flash('Your booking has been submitted successfully!', 'success')
        return redirect(url_for('booking_confirmation'))
    
    return render_template('booking.html', vehicles=vehicles)

@app.route('/booking/confirmation')
def booking_confirmation():
    return render_template('booking_confirmation.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
