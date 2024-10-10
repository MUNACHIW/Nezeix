const validation = () => {
    var email = document.getElementById('email').value;

    if (email.trim() == "") {
        alert("Fill in your email address")
        return false
    } else {
        alert("Subscribed successfully")
        return true
    }
}