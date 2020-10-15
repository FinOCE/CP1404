from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi('Fancy Taxi', 100, 2)
    taxi.drive(50)
    print(taxi)

main()