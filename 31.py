while True:
    try:
        year_birth = int(input("Enter the year of your birth:\n", ));
        print(15/year_birth);
    except ValueError:
        print("Enter the integer number,please");
    except ZeroDivisionError:
        print("Enter integer numbers besides zero!")
    except:
        break;
    finally:
        print("Thank you")


