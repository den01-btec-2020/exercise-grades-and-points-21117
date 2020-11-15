def main():
    #write your code below this line
    sc = input("Enter score between 0-100")
    fl_sc = float(sc)

    if fl_sc <0:
      gr = "Impossible"
    elif fl_sc <49:
      gr = "Failed"
    elif fl_sc <59:
      gr = "1"
    elif fl_sc <69:
      gr = "2"
    elif fl_sc <79:
      gr = "3"
    elif fl_sc <89:
      gr = "4"
    elif fl_sc <99:
      gr = "5"
    elif fl_sc >100:
      gr = "incredible"

    print("Score", fl_sc, "grade", gr)
  

if __name__ == '__main__':
    main()
