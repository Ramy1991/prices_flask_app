$( document ).ready(function() {
var firebaseConfig = {
            apiKey: "AIzaSyCQYdl0vf8gKnayNRM18dbfMpYIQxzi0LI",
            authDomain: "bright-lattice-260000.firebaseapp.com",
            databaseURL: "https://bright-lattice-260000.firebaseio.com",
            projectId: "bright-lattice-260000",
            // storageBucket: "bright-lattice-260000.appspot.com",
            // messagingSenderId: "1014243229877",
            // appId: "1:1014243229877:web:71f55e2379e3c05a8bfefc",
            // measurementId: "G-275CEDTFV7"
        };
        firebase.initializeApp(firebaseConfig);
        var db = firebase.firestore();
        firebase.auth().useDeviceLanguage();
        // var dbRef = firebase.database().ref("users");
        function switch_form(){
            // $('#sign_in_box').addClass('target');
            $( "#sign_up_link" ).click(function(e) {
                e.preventDefault();
                $('#sign_in_box').addClass('target');
                $('#sign_up_box').removeClass('target');           
                window.scrollTo(0, 5000);
            });
            $( "#login_link" ).click(function(e) {
                e.preventDefault();
                $('#sign_up_box').addClass('target');
                $('#sign_in_box').removeClass('target');
            });
        }

        switch_form();

        $('.btn-header').click(function(e){
            e.preventDefault();
            $('body,html').animate({ scrollTop: $('body').height() }, 1200);
            var name_id = $(this).attr('name');
            if(name_id == 'sign_in'){
                $( "#login_link" ).click();
            }else{
                $( "#sign_up_link" ).click();
            }
        });

        // function validation(db, name, inputs){
        //     db.collection("users").where(name, "==", inputs).limit(1).get().then(function(snap) {
        //         if(!snap.empty){
        //             $('#' + name + '_e').css('display','block');
        //             $('#' + name).addClass('is-invalid');
        //         }else{ 
        //             $('#' + name + '_e').css('display','none');
        //             $('#' + name).removeClass('is-invalid');
        //         }
        //     }).catch(function(error){
        //         console.log(error.message);
        //     });
        // }

        // $('.validation').keyup(function(){
        //     var inputs = $(this).val();
        //     var name = $(this).attr('name');
        //     validation(db, name, inputs);
           
        // });

        function pw_validation(p1, p2){
            if (p1 != p2) {
                $('#pwc_e').css('display','block');
                $('#confirm_pw').addClass('is-invalid');
                return false;
            }else{
                $('#pwc_e').css('display','none');
                $('#confirm_pw').removeClass('is-invalid');
                return true;
            }    
        }

        $('.pw_v').keyup(function(){
            var pw = $('#s_pw').val();
            var confirm_pw = $('#confirm_pw').val();
            pw_validation(pw, confirm_pw);
        });

        function writeuserdateFB(email, username, pw, auth){
            firebase.database().ref('users/' + auth).set({
                'email': email,
                'username': username,
                'password': pw,
                'id': auth,
                'num_of_t_items': 0,
                'tier': 'free_user_5',
                'tracking_uids': 0,
                'tracking_items': 0

            }).then(function(){
                onAuthStateChanged();
            }).catch(function(err){
                console.log(err);
            })
        }

        function writeUserData(email, username, pw, auth) {
            db.collection("users").doc(auth).set({
                email: email,
                username: username,
                password: pw,
                id: auth,
                num_of_t_items: 0,
                tier: 'free_user_5',
                tracking_uids: [],
                tracking_items: {}
            }).then(function(){
                writeuserdateFB(email, username, pw, auth)
            }).catch(function(error) {
                console.log("Error: " + error.message);
            });
        }

        function sign_in_with_provider(provider){
            firebase.auth().signInWithPopup(provider).then(function(result) {
                db.collection("users").doc(result.user.uid).get().then(function(snapshot) {
                    if(snapshot.exists){ 
                        onAuthStateChanged(); 
                    }else{          
                        var user_current = firebase.auth().currentUser;
                        var pw = Math.random().toString(36).slice(-8);
                        user_current.updatePassword(pw).then(function() {
                            console.log("done");
                        }).catch(function(error) {
                            console.log(error.message);
                        }).then(function(){
                            writeUserData(result.user.email, result.user.displayName, pw, result.user.uid);
                        });
                    }
                }).catch(function(error) {
                    console.log(error.message);
                });
            }).catch(function(error) {
                console.log(error.message); 
            });
        }
       
        $('.social-auth').click(function(e){
            e.preventDefault();
            var socaial_provider = $(this).attr('name');
            if (socaial_provider == "Facebook"){
                var provider = new firebase.auth.FacebookAuthProvider();
            }else{
                var provider = new firebase.auth.GoogleAuthProvider();
            }
            sign_in_with_provider(provider);

        });

        $('#login_form').submit(function (e) {
            e.preventDefault();
            var sign_in_email = $('#email').val();
            var sign_in_pass = $('#password').val();
            firebase.auth().signInWithEmailAndPassword(sign_in_email, sign_in_pass).then(function(snap) {
                console.log("snap");
                onAuthStateChanged();
            }).catch(function(error){
                alert(error.message);
            })
        });

        $('#sign_up_form').submit(function (e) {
            e.preventDefault();
            var email = $('#s_email').val();
            var username = $('#s_username').val();
            var pw = $('#s_pw').val();
            var confirm_pw = $('#confirm_pw').val();
            if (pw_validation(pw, confirm_pw) === true){
                firebase.auth().createUserWithEmailAndPassword(email, pw).then(function() {
                    if (firebase.auth().currentUser !== null) {
                        writeUserData(email, username, pw, firebase.auth().currentUser.uid);
                    }
                }).catch(function(error){
                    // alert(error.message);
                    $('#email_e').css('display','block');
                    $('#email').addClass('is-invalid');
                });
            }else{
                alert('Password Don\'t Match');
            }
        });
        function onAuthStateChanged(){
            firebase.auth().onAuthStateChanged(function(user) {
                if (user) {
                    window.location = window.location.href + 'user/' + user.displayName.replace(/\s+/g, '-').toLowerCase();
                } 
            });
        }
        
        $('#reset-password').submit(function(e){
            e.preventDefault();
            var emailAddress = $("#email-address").val();
            firebase.auth().sendPasswordResetEmail(emailAddress).then(function() {
                $('#email-sent').css('display','block');
                $('#email-address').css('display','none');
                $('#email-sent').css('color','green');
                $('#email-sent').html("Email Sent Successfully <i class='fa fa-check'></i>");
                setTimeout(function() { $('.close').click(); }, 3000);
            }).catch(function(error) {
                $('#email-sent').css('display','block');
                $('#email-sent').css('color','red');
                $('#email-sent').html('There is no user on our records with this Email Address. or This user may have been deleted.');
            });
        });

        $('.close-pop').click(function(){
            $('#email-sent').css('display','none');
            $('#email-address').css('display','block');
            $('#email-sent').html('');
        });

        });
        // $.ajax({
        //     url: "https://egypt.souq.com/eg-en/",
        //     method: "GET",
        //     dataType: "jsonp",
        //     crossDomain: true
        // });


        // fetch('https://egypt.souq.com/eg-en/',{mode: 'cors'}).then((response) => {
        //     return response.json();
        // }).then((myJson) => {
        //     console.log(myJson);
        // });