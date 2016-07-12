
from Fleet import Fleet

def run():
    disp = """
	**************************************************
    *  0. status                                     *
	*  1. Rent A Car   				                 *
	*  2. Return Car 				                 *
    *  3. Rent A Truck                               *
    *  4. Return A Truck                             *
    *  5. service a truck                            *
    *  6. service a car                              *
    *  7. add new car                                *
    *  8. add new truck                              *
    *  9. exit program                               *
	**************************************************
    """
    i = 1
    fleet = Fleet()

    while(i>0):
        print(disp)
        cmd = input("Enter input 0-9:")
        if cmd == '9':
            i = -1
        elif cmd == '0':
            print(fleet.get_status())
        elif cmd == '1':
            print(fleet.rent_car())
        elif cmd == '2':
            print(fleet.return_car())
        elif cmd == '7':
            print(fleet.add_car())


if __name__ == '__main__':
    run()
