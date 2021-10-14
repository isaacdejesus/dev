package com.example.aboutme

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.view.inputmethod.InputMethodManager
import androidx.databinding.DataBindingUtil
import com.example.aboutme.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    //object used for data binding.
    //data binding creates an object that allows us to access views directly without having
    //to go through view hierarchy in order to find the view
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //setContentView(R.layout.activity_main)
        //bind the object to activity main view hierarchy
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        //when button is clicked, addNickname function is called
        //views are accessed simply by binding.viewId, where id = view_id
        binding.doneButton.setOnClickListener {
            addNickname(it)
        }
    }

    private fun addNickname(view: View)
    {
        binding.apply {
            //set text to value entered by user
            nicknameText.text = binding.nicknameEdit.text
            invalidateAll()
            //hide field and button
            nicknameEdit.visibility = View.GONE
            doneButton.visibility = View.GONE
            //display text
            nicknameText.visibility = View.VISIBLE
        }
        //code to hide keyboard
        val imm = getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
        imm.hideSoftInputFromWindow(view.windowToken, 0)
    }
}