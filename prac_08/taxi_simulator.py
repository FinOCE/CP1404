from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():
    current_taxi = None
    total_bill = 0

    response = get_menu_response(current_taxi, total_bill)
    while response != 'q':
        if response == 'c':
            current_taxi = choose_taxi()
            response = get_menu_response(current_taxi, total_bill)
        elif response == 'd':
            total_bill = drive_taxi(current_taxi, total_bill)
            response = get_menu_response(current_taxi, total_bill)
        else:
            invalid_response()
            response = get_menu_response(current_taxi, total_bill)
    print(f'Total trip cost: ${total_bill:.2f}')
    print('Taxis are now:')
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')

def get_menu_response(current_taxi, total_bill):
    if current_taxi != None:
        print(f'Billed to date: ${total_bill:.2f}')
    print('q)uit, c)hoose taxi, d)rive')
    return input('>>> ').lower()

def invalid_response():
    print('Invalid response. Please try again.')

def choose_taxi():
    print('Taxis available:')
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')
    chosen_valid_taxi = False
    while chosen_valid_taxi == False:
        try:
            chosen_taxi = int(input('Choose taxi: '))
            while chosen_taxi >= len(taxis) or chosen_taxi < 0:
                invalid_response()
                chosen_taxi = int(input('Choose taxi: '))
            chosen_valid_taxi = True
        except ValueError:
            invalid_response()
    return taxis[chosen_taxi]

def drive_taxi(current_taxi, total_bill):
    if current_taxi != None:
        driven_valid_distance = False
        while driven_valid_distance == False:
            try:
                distance = float(input('Drive how far? '))
                while distance < 0:
                    invalid_response()
                    distance = float(input('Drive how far? '))
                driven_valid_distance = True
            except ValueError:
                invalid_response()
        current_taxi.start_fare()
        current_taxi.drive(distance)
        print(f'Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}')
        total_bill += current_taxi.get_fare()
        return total_bill
    else:
        print('You must choose a taxi before you drive.')

main()