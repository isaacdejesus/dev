package com.example.viewsapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.graphics.Color
import android.graphics.Color.LTGRAY
import android.widget.Button
import android.widget.TextView
import org.w3c.dom.Text

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setListeners()
    }

    private fun makeColored(view: View)
    {
        val box3 = findViewById<TextView>(R.id.box_three_text)
        val box4 = findViewById<TextView>(R.id.box_four_text)
        val box5 = findViewById<TextView>(R.id.box_five_text)
        when (view.id)
        {
            // Boxes using Color class colors for the background
            R.id.box_one_text -> view.setBackgroundColor(Color.DKGRAY)
            R.id.box_two_text -> view.setBackgroundColor(Color.GRAY)
            R.id.box_three_text -> view.setBackgroundColor(Color.BLUE)
            R.id.box_four_text -> view.setBackgroundColor(Color.MAGENTA)
            R.id.box_five_text -> view.setBackgroundColor(Color.GREEN)

            R.id.red_button -> box3.setBackgroundResource(R.color.my_red)
            R.id.yellow_button -> box4.setBackgroundResource(R.color.my_yellow)
            R.id.green_button -> box5.setBackgroundResource(R.color.my_green)
            else -> view.setBackgroundColor(Color.LTGRAY)
        }
    }
    private fun setListeners() {

        val boxOneText = findViewById<TextView>(R.id.box_one_text)
        val boxTwoText = findViewById<TextView>(R.id.box_two_text)
        val boxThreeText = findViewById<TextView>(R.id.box_three_text)
        val boxFourText = findViewById<TextView>(R.id.box_four_text)
        val boxFiveText = findViewById<TextView>(R.id.box_five_text)

        val rootConstraintLayout = findViewById<View>(R.id.constraint_layout)

        val redButton = findViewById<Button>(R.id.red_button)
        val greenButton = findViewById<Button>(R.id.green_button)
        val yellowButton = findViewById<Button>(R.id.yellow_button)
        val clickableViews: List<View> =
            listOf(boxOneText, boxTwoText, boxThreeText, boxFiveText, boxFourText,
                redButton, greenButton, yellowButton, rootConstraintLayout)

        for (item in clickableViews){
           item.setOnClickListener{makeColored(it)}
        }
    }

}