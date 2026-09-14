while true

do
  echo "1. Add"
  echo "2. Subtract"
  echo "3. Multiply"
  echo "4. Divide"
  echo "5. Quit"

  read -p "enter your choice" choice

  if [ $choice -eq 1 ]
  then
      read -p "Enter number 1: " number1
      read -p "Enter number 2: " number2
      echo Answer=$(( $number1 + $number2 ))

  elif [ $choice -eq 2 ]
  then
     read -p "Enter number 1: " number1
     read -p "Enter number 2: " number2
     echo Answer=$(( $number1 - $number2 ))

  elif [ $choice -eq 3 ]
  then
     read -p "Enter number 1: " number1
     read -p "Enter number 2: " number2
     echo Answer=$(( $number1 * $number2 ))

  elif [ $choice -eq 4 ]
  then
     read -p "Enter number 1: " number1
     read -p "Enter number 2: " number2
     echo Answer=$(( $number1 / $number2 ))

 elif [ $choice -eq 5 ]
 then 
    break
fi

done
---------------------------------------------------------------------

while true
do
  echo "1. Add"
  echo "2. Subtract"
  echo "3. Multiply"
  echo "4. Divide"
  echo "5. Quit"

  read -p "Enter your choice: " choice

  case $choice in
    1)
        read -p "Enter Number1: " number1
        read -p "Enter Number2: " number2
        echo Answer=$(( $number1 + $number2 ))
        ;;
    2)
        read -p "Enter Number1: " number1
        read -p "Enter Number2: " number2
        echo Answer=$(( $number1 - $number2 ))
        ;;

    3)
        read -p "Enter Number1: " number1
        read -p "Enter Number2: " number2
        echo Answer=$(( $number1 * $number2 ))
        ;;
    4)
        read -p "Enter Number1: " number1
        read -p "Enter Number2: " number2
        echo Answer=$(( $number1 / $number2 ))
        ;;
    5)
        break
        ;;
  esac

done