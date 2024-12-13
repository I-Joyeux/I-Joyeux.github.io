"use strict";

function validateEmailList() {
    // get values user entered in text boxes
    const email_1 = $("#email_1").val();
    const email_2 = $("#email_2").val();
    const first_name = $("#first_name").val();
    const emailPattern = /^[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]+$/; //join pattern

    let isValid = true;

    // check user entries and alrt if invalid
    if (email_1 == "") { 
        isValid = false;
        $("#email_1").next().text("This field is required.");
    } else if (!emailPattern.test(email_1)) {
        $("#email_1").next().text("please enter email format");
    } else {
        $("#email_1").next().text("");
    }

    if (email_2 == "") 
    { 
        isValid = false;
        $("#email_2").next().text("Please confirm your email.");
    } 
    else if (email_1 != email_2) 
    { 
        isValid = false;
        $("#email_2").next().text("Email must match.");
    } 
    else 
    {
        $("#email_2").next().text("");
    }

    if (first_name === "")
     {
        isValid = false;
        $("#first_name").next().text("First name is required.");
    } 
    else {
        $("#first_name").next().text("");
    }

    // replace form with confirmation text if form entries are valid
    const head = $("#head");
    if (isValid) {
        head.text("Thank you: " + $("#first_name").val());    //message if submitted with all the requirement
        $("#email_1").val("")
        $("#email_2").val("");
        $("#first_name").val("");
        
    }
}

$(document).ready(() => {
    const messageValue = $("#message");


    $("#join_list").click(() => {
        validateEmailList();    
    });

    $("#emailForm").keydown(() => {
        if (event.key === "Enter") { 
            validateEmailList();
        }
    });

    $("#clear_form").click(() => {
        messageValue.text("");
        $("#email_1").val("")
        $("#email_2").val("");
        $("#first_name").val("");

        $("#email_1").next().text("");
        $("#email_2").next().text("");
        $("#first_name").next().text("");
        $("#email_1").focus();
    });
    $("#email_1").focus();
});