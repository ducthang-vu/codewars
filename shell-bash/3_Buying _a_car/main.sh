#!/bin/bash

# Buying a car
# https://www.codewars.com/kata/554a44516729e4d80b000012/train/shell

# A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. He wants to keep his old car until he can buy the secondhand one.

# He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months. Our man finds it difficult to make all these calculations.

# Can you help him?

# How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over?

nbMonths() {
   priceOld=$1
   priceNew=$2 
   savingperMonth=$3
   percentLossByMonth=$4
   savings=0
   month=0
   while [ "$savings" -lt "$priceNew" ]
   do
      echo ${saving}
      let remainder=month%2
      if [[ $remainder -eq 0 ]] ; then
         let percentLossByMonth = $percentLossByMonth" + "1.5" 
      fi
      let "month++"
      let savings+=savingperMonth
   done

}
nbMonths $1 $2 $3 $4