$(document).ready(function () {
    
    $(document).on("submit", "#contact-form-ajax", function (e) {
        e.preventDefault()
        console.log("Submited...");

        let full_name = $("#full_name").val()
        let email = $("#email").val()
        let phone = $("#phone").val()
        let subject = $("#subject").val()
        let message = $("#message").val()

        console.log("Name:", full_name);
        console.log("Email:", email);
        console.log("Phone:", phone);
        console.log("Subject:", subject);
        console.log("MEssage:", message);

        $.ajax({
            url: "/ajax-contact-form",
            data: {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "subject": subject,
                "message": message,
            },
            dataType: "json",
            beforeSend: function () {
                console.log("Sending Data to Server...");
            },
            success: function (res) {
                console.log("Sent Data to server!");
                $(".contact_us_p").hide()
                $("#contact-form-ajax").hide()
                $("#message-response").html("Message sent successfully.")
            }
        })
    })

    $(document).on("submit", "#get-quote-ajax", function (e) {
        e.preventDefault();
        console.log("Submitted...");
    
        let email = $("#email-1").val();
        console.log("Email:", email);
    
        // Email validation using regular expression
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            $("#email-error").html("Please enter a valid email address").addClass("text-danger");
            return;  // Stop the form submission if the email is not valid
        } else {
            $("#email-error").html("").removeClass("text-danger");
        }
    
        $.ajax({
            url: "/ajax-get-quote",
            data: {
                "email": email,
            },
            dataType: "json",
            beforeSend: function () {
                console.log("Sending Data to Server...");
            },
            success: function (res) {
                console.log("Sent Data to server!");
                $(".get_quote_hide").hide();
                $("#get-quote-ajax").hide();
                $("#confirmation").html("Will get back to you soon!").removeClass("text-danger").addClass("text-success");
            }
        });
    });    
})