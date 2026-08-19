month_number=$1

if [ -z $month_number ]
then
   echo "No month number given. Provide month number as an argument"
   echo " e.g ./print-month-number.sh 5 "
   exit
fi


if [[ month_number -lt 1 ]] || [[ month_number -gt 12 ]]
then
    echo "Not a valid month number"
    exit
fi

if [ $month_number -eq 1 ]
then
   echo "January"
elif [ $month_number -eq 2 ]
then
   echo "Feburary"
elif [ $month_number -eq 3 ]
then
   echo "March"
elif [ $month_number -eq 4 ]
then
   echo "April"
elif [ $month_number -eq 5 ]
then
   echo "May"
elif [ $month_number -eq 6 ]
then
   echo "June"
elif [ $month_number -eq 7 ]
then
   echo "July"
elif [ $month_number -eq 8 ]
then
   echo "August"
elif [ $month_number -eq 9 ]
then
    echo "September"
elif [ $month_number -eq 10 ]
then
    echo "October"
elif [ $month_number -eq 11 ]
then
    echo "November"
elif [ $month_number -eq 12 ]
then
    echo "December"
fi