 const firebaseConfig = {
    apiKey: "AIzaSyCkuzhvKkEUKEj5XXIhIKMDBovlrxyZF9A",
    authDomain: "contact-form-73d1c.firebaseapp.com",
    databaseURL: "https://contact-form-73d1c-default-rtdb.firebaseio.com",
    projectId: "contact-form-73d1c",
    storageBucket: "contact-form-73d1c.appspot.com",
    messagingSenderId: "564775523666",
    appId: "1:564775523666:web:6fcdbd1648d30f3b1d968b",
    measurementId: "G-RMX5GE3BLH"
};

//initialize firebase  
firebase.initializeApp(firebaseConfig);

//reference ur database
const contactFormDB = firebase.database().ref("contact-form");

document.getElementById('contactForm').addEventListener("submit", submitForm);


function submitForm(e) {
    e.preventDefault();

    var name = getElementval('name');
    var email = getElementval('email');
    var messagecnt = getElementval('messagecnt');

    saveMessages(name, email, messagecnt);

    //enable the alert

    document.querySelector(".alert").style.display = "block";
    
    //remove the alert

    setTimeout(() => {
         document.querySelector(".alert").style.display = "none";
    }, 3000);

   //reset the form

    document.getElementById("contactForm").reset();
}

const saveMessages = (name, email, messagecnt) => {
    var newContactForm = contactFormDB.push();
    newContactForm.set({
        name: name,
        email: email,
        messagecnt: messagecnt,
    });
};

const getElementval = (id) => {
    return document.getElementById(id).value;
};




