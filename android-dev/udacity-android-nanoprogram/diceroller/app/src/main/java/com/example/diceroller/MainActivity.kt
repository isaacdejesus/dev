package com.example.diceroller

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
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
    }

    private fun rollDice() {
        val resultText: TextView = findViewById(R.id.result_text)
        val randomInt = Random.nextInt(6)+ 1
        resultText.text = randomInt.toString()
    }
}