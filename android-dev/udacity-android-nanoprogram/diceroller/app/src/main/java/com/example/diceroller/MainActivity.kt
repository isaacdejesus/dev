package com.example.diceroller

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    //saves reference to images in a field leading to performance gain since
    //no longer need to call findviewbyid every time dice is rolled.
    lateinit var diceImage: ImageView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Obtain view by id. In this case button
        //assign it to a var which allows us to manipulate/change contents
        val rollButton: Button = findViewById<Button>(R.id.roll_button)
        rollButton.setOnClickListener{
            //calls function rollDice whenever button is clicked
            rollDice()
        }
        diceImage = findViewById(R.id.dice_image)
    }

    private fun rollDice() {
        val randomInt = Random.nextInt(6)+ 1

        //saves image returned by when statement into drawableResource
        val drawableResource = when (randomInt)
        {
            1-> R.drawable.dice_1
            2-> R.drawable.dice_2
            3-> R.drawable.dice_3
            4-> R.drawable.dice_4
            5-> R.drawable.dice_5
            else -> R.drawable.dice_6
        }
        //set/change image displayed by view to values/image obtained from when statement
        diceImage.setImageResource(drawableResource)
    }
}