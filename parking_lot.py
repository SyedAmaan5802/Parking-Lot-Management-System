class Vehicle:
    def __init__(self, v_type, plate):
        self.type = v_type
        self.plate = plate
        self.entry_time = None

    def set_entry_time(self, entry_time):
        self.entry_time = entry_time

    def get_type(self):
        return self.type

    def get_plate(self):
        return self.plate

    def get_entry_time(self):
        return self.entry_time


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity
        self.spaces = [None] * capacity

    def is_full(self):
        return self.available_spaces == 0

    def park_vehicle(self, vehicle):
        if self.is_full():
            return "Parking lot is full."

        for i in range(self.capacity):
            if not self.spaces[i]:
                self.spaces[i] = vehicle
                self.available_spaces -= 1
                return f"Vehicle with plate {vehicle.get_plate()} parked at space {i+1}."

    def exit_vehicle(self, plate):
        for i in range(self.capacity):
            if self.spaces[i] and self.spaces[i].get_plate() == plate:
                vehicle = self.spaces[i]
                self.spaces[i] = None
                self.available_spaces += 1
                return vehicle
        return None

    def view_vehicle(self, plate):
        for i in range(self.capacity):
            if self.spaces[i] and self.spaces[i].get_plate() == plate:
                vehicle = self.spaces[i]
                return f"Vehicle Type: {vehicle.get_type()}, Plate: {vehicle.get_plate()}, Entry Time: {vehicle.get_entry_time()}"
        return "Vehicle not found in the parking lot."

    def display_lot_status(self):
        print("\nParking Lot Status:")
        for i in range(self.capacity):
            if self.spaces[i]:
                print(f"Space {i+1}: {self.spaces[i].get_plate()} (Type: {self.spaces[i].get_type()})")
            else:
                print(f"Space {i+1}: Empty")

    def calculate_fare(self, vehicle, exit_time):
        total_time = exit_time - vehicle.get_entry_time()
        hours = total_time / 3600

        if vehicle.get_type() == 1:  # Car
            rate = 150 * hours
        elif vehicle.get_type() == 2:  # Truck
            rate = 200 * hours
        elif vehicle.get_type() == 3:  # Motorcycle
            rate = 100 * hours
        else:
            rate = 0

        return round(rate, 2)


def main():
    capacity = 10
    parking_lot = ParkingLot(capacity)

    while True:
        print("\nWelcome to the Parking Lot Management System!")
        print("1. Park a vehicle")
        print("2. Exit a vehicle")
        print("3. View a vehicle")
        print("4. Display parking lot status")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            v_type = int(input("Enter vehicle type (1 for Car, 2 for Truck, 3 for Motorcycle): "))
            plate = input("Enter vehicle plate number: ")
            vehicle = Vehicle(v_type, plate)
            entry_time = time.time()
            vehicle.set_entry_time(entry_time)
            message = parking_lot.park_vehicle(vehicle)
            print(message)

        elif choice == "2":
            plate = input("Enter vehicle plate number: ")
            exit_time = time.time()
            vehicle = parking_lot.exit_vehicle(plate)
            if vehicle:
                fare = parking_lot.calculate_fare(vehicle, exit_time)
                print(f"Vehicle with plate {plate} exited.")
                print(f"Total Fare: ₹{fare}")
            else:
                print(f"Vehicle with plate {plate} not found in the parking lot.")

        elif choice == "3":
            plate = input("Enter vehicle plate number: ")
            info = parking_lot.view_vehicle(plate)
            print(info)

        elif choice == "4":
            parking_lot.display_lot_status()

        elif choice == "5":
            print("Thank you for using the Parking Lot Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    import time
    main()
