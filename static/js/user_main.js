import { initializeApp } from "https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.1.3/firebase-auth.js";
import { getDatabase, ref, onValue, set, update, remove, get, child } from 'https://www.gstatic.com/firebasejs/9.1.3/firebase-database.js';


const firebaseConfig = {
    apiKey: "AIzaSyCQYdl0vf8gKnayNRM18dbfMpYIQxzi0LI",
    authDomain: "bright-lattice-260000.firebaseapp.com",
    databaseURL: "https://bright-lattice-260000.firebaseio.com",
    projectId: "bright-lattice-260000",
    storageBucket: "bright-lattice-260000.appspot.com",
    messagingSenderId: "1014243229877",
    appId: "1:1014243229877:web:71f55e2379e3c05a8bfefc",
    measurementId: "G-275CEDTFV7"
};
const app = initializeApp(firebaseConfig);
const auth = getAuth();
const db = getDatabase();
// const user = auth.currentUser;
// const user = auth.currentUser;
// firebase.initializeApp(firebaseConfig);


onAuthStateChanged(auth, (user) => {
    // const user = auth.currentUser;
    // console.log(user);
    const c_url = window.location.href.split('/')[5].replace('#','');
    const u_url = user.displayName.replace(" ", "-").toLowerCase();
    
    if (user && (c_url === u_url)) {
        $("#user").text("Hello, " + user.displayName);
        $('#products-articles').css('display','');
        $("#status").html("Dashboard")
        load_user_items(user);
        request_to_add_item(user);
    } else {
        setTimeout(() => {  $("#status").html("404 Error"); }, 100);
    }   
});


function load_user_items(user){
    const db = getDatabase();
    const user_data = ref(db, 'users/' + user.uid);
    onValue(user_data, (usersnap) => {
        const count_of_item = usersnap.val().num_of_t_items;
        var n = [];
        const items_html  = $('<div>', { class:'row articles', id: 'products-container'});
        // console.log(count_of_item);
        if (count_of_item != 0){
            $.each(usersnap.val().tracking_items, function(uids, vals){
                const item_curr = vals.currancy;
                const items_data = ref(db, 'p_p_data/' + vals.item_uid);
                onValue(items_data, (productsnap) => {
                    $.each(productsnap.val().item_price, function(currsnap, item_p_date) {
                        if (currsnap === item_curr){
                            // console.log(Object.values(item_p_date).sort().reverse()[0].price);
                            var item_p_last = Object.values(item_p_date).sort().reverse()[0].price
                            items_html.append(html_item(productsnap.val(), item_p_last, item_curr))
                        }
                    });
                    n.push("1");
                    if (n.length === Object.keys(usersnap.val().tracking_items).length){
                        $("#products-articles").empty().removeClass('row articles').html(items_html)
                        pro_num(Object.keys(usersnap.val().tracking_items).length)
                        $("#loading_main_page").css('display','none');
                        on_remove(user.uid);
                        on_replace();
                        close_pop();
                    }
                });
      
            });
        } else {
            $("#loading_main_page").css('display','none');
            $("#products-articles").empty().removeClass('row articles').append(items_html);
            pro_num(0);
        }    
    });
}



function request_to_add_item(user){
    $('.add-item').click(function(e){
        var item_url = $("#item-link").val()
        if(!item_url){
            var item_url = $("#size-list").val();
        }
        var price_target = $('#price_note').val();
        if(item_url && $.isNumeric(price_target) || !price_target){
            e.preventDefault();
            $('.botton-d, .add-item').prop('disabled', true);
            $('#loading_add_item').css('display','block');
            $("#add_item_panel, .err_load_data, #select_dialog").css('display','none');
            $('.btn-d, .add-item').addClass('disabled');
            // $('#add-item').addClass('disabled')
            $.ajax({
                type: "POST",
                url: '/get_item_data',
                data: {name: item_url}
            }).done(function(data){
                console.log(data);
                if (data.trim().includes("dummy_website")){
                    console.log(data);
                    // $('.botton-d, .add-item').prop('disabled', false);
                    $('.btn-d, .add-item').addClass('disabled');
                    // $('#loading_add_item').css('display','none');
                    $('#add_item_panel, .err_load_data').css('display','block');
                }else if(data.trim().includes("missing_data")){
                    console.log(data);
                    // $('.botton-d, .add-item').prop('disabled', false);
                    // $('.btn-d, .add-item').removeClass('disabled');
                    // $('#loading_add_item').css('display','none');
                    $('.err_load_data').html('* Error Loading Data');
                    $('#add_item_panel, .err_load_data').css('display','block');
                    console.log('hello');
                }else if(!data.trim().includes("item_uid")){
                    $('#item-link').val('');
                    get_size_url(data, item_url);
                }else{
                    try {
                        console.log(data);
                        var item_data = JSON.parse(data);
                        if(e.target.id){
                            $.when(
                                remove_item(user.uid, e.target.id)
                            ).then(
                                add_item(item_data, user.uid, price_target)
                            );
                        }else{
                            add_item(item_data, user.uid, price_target)
                        }
                    }catch(err) {
                        alert(err);
                    }finally{
                        $('#myModal').modal('hide');
                        $('#add_item_panel').css('display','');
                        $('#item-link, #price_note').val('');
                    }
                }
                $('#loading_add_item').css('display','none');
                $('.botton-d, .add-item').prop('disabled', false);
                $('.btn-d, .add-item').removeClass('disabled')
                close_pop();
            });
        }else{
            alert('Please Set URL Field and target price should be Number')
        }
    });
}    


$('#size-list').on('change', function() {

    $('.add-item').addClass('disabled');
    $('#price_range').css('opacity', '0.4');
    $('.loading_price').css('display', '');
    $('.add-item').prop('disabled', true);
    $.ajax({
        type: "POST",
        url: '/get_item_data',
        data: {name: this.value}
    }).done(function(data1){
        console.log(data1)
        if(data1.trim().includes("missing_data: item_price")){
            $('#price_range').text('out of stock')
        }else if(data1.trim().includes("missing_data")){
            console.log(data1)
            $('.err_load_data').css('display','');
        }else{
            var item_data = JSON.parse(data1);
            if(item_data.item_price == 'out of stock'){
                $('#price_range').text(item_data.item_price)
            }else{
                $('#price_range').text(item_data.item_price + ' ' + item_data.currency);
            }
        }
       $('.add-item').removeClass('disabled');
       $('.loading_price').css('display', 'none');
       $('#price_range').css('opacity', '1');
       $('.add-item').prop('disabled', false);
    });

});


function get_size_url(data, item_url){
    $('#loading_add_item').css('display','none');
    $('#select_dialog').css('display','block');
    var item_info = JSON.parse(data);
    console.log(item_info);
    var title = item_info.item_title;
    var img = item_info.item_image;
    var price_data = item_info.item_price;
    var size_data = item_info.item_sizes;
    $('#title').text(title);
    $('#item-img').attr("src", img);
    if(price_data.includes("missing_data")){
        price_data = 'out of stock'
    }
    $('#price_range').text(price_data);
    var option = ['<option value=""> Select </option>']
    for(key in size_data){
        UID = size_data[key];
        option.push(' <option value="https://' + item_url.split('/')[2] + '/dp/' + UID.split(',')[1] + '?language=en&th=1&psc=1">' + key + '</option>')
    }
    $('#size-list').html(option.join(''));
}

function html_item(item_data, item_price, item_curr){
    if (item_price == "Out of Stock"){
        item_price = item_price
    }else{
        item_price = item_price + ' ' + item_curr
    }
    var product_template = $('<div>',{ id: item_data.item_uid, class: 'col-sm-6 col-md-4 item'});
    var a_delete_ele = $('<a>',{ class: 'a_del_item tooltap'});
        a_delete_ele.append($('<img>', {class: 'trash_icon',src: '/static/img/stop.svg'}), $('<span>',{class: 'tooltaptext', text: 'Delete Item' }));
    var item_img_ele = $('<a>', {href: '#'}).append($('<div>',{class: 'image_box' }).append($('<img>',{class: 'img-fluid', src: item_data.item_image})));
    var item_title_ele = $('<div>').append($('<h3>', {class: 'name name2'}).append('<br/>',$('<p>', {text: item_data.item_title}).css({"font-size": "15px", "font-weight": "600","color":"#333"})));
    var item_price_ele = $('<p>', {text: item_price, class: 'description'});
    var btn_buy_ele = $('<button>', {class: 'btn btn_buy', type: 'button', text: 'Buy Now' }).append($('<i>', {class: 'typcn typcn-shopping-cart icon'}));
    var item_link_ele = $('<a>', {href: item_data.item_url, target: '_blank'}).append(btn_buy_ele);
    var change_item_ele = $('<div>',{class: 'btn_change_link'}).append($('<a>',{class: 'link rep_item',role: 'button', 'data-toggle': 'modal', href: '#myModal', text: 'Change Item'}));
    var footer_ele = $('<div>', {class: 'botton_group'}).css("padding-top", "16px").append(item_link_ele, change_item_ele);
        product_template.append(a_delete_ele, item_img_ele, item_title_ele, item_price_ele, footer_ele);
    return  product_template;
}

function pro_num(user_pro_num){
    var html_add_item = $('<div>',{class: 'col-sm-6 col-md-4 item'}).append(
        $('<a>',{href: '#myModal', 'data-toggle': 'modal', class: 'botton-d '}).append(
            $('<img>',{class: 'img-fluid link-model', src: '/static/img/add-link.png'}),
            $('<h3>'),
            $('<h3>',{class: 'name btn btn-d', text: 'Click to Add Product Link'}).css({'border': '1px solid #7d8285','border-radius': '3px','position': 'absolute', 'bottom': '-19px', 'margin': 'auto','min-width': '212px', 'left':'50%', 'transform': 'translate(-50%, -50%)'})
    ));
    var items_count = 6 - user_pro_num;
    for (var i = 1; i <= items_count; i++) {
        $( "#products-container" ).append( html_add_item.clone()) ;
    }
}

function add_item(item_data, auth, price_target){
    if (/[\u0600-\u06FF]/.test(item_data.item_uid)){
        item_uid = item_data.item_url.replace(/\.|\//g, '_');
    }
    add_item_ppdata(item_data, auth, price_target)
}

function add_item_ppdata(item_data, auth, price_target){
    var price = item_data.item_price
    const load_db = ref(db, 'p_p_data/' +  item_data.item_uid);
    const dbRef = ref(getDatabase());
    get(child(dbRef, 'p_p_data/' +  item_data.item_uid)).then((productsnappp) => {
        if(productsnappp.val() === null){
            set(ref(db, 'p_p_data/' + item_data.item_uid), {
            // firebase.database().ref('p_p_data/' + item_data.item_uid).set({
                "item_image": item_data.item_image,
                "item_title": item_data.item_title,
                "item_uid": item_data.item_uid,
                "item_url": item_data.item_url,
                "created_date": item_data.date,
                "item_website": item_data.item_website,
                "pool": 1,
                "users_tracking_num": 1,
                "item_price":   {[item_data.currency]: {
                                        [item_data.date + ' ' + item_data.time]: {
                                        "date_time": item_data.date + ' ' + item_data.time,
                                        "price": item_data.item_price
                                        }
                                    }
                                }
            }).then(function(){
                add_item_user(auth, item_data, price_target);
            }).catch(function(error) {
                console.log(error.message);
            });
        }else{
            update_tracking_item(item_data.item_uid, "add");
            add_item_user(auth , item_data, price_target);
        }
    })
}

function add_item_user(auth , item_data, price_target){
    const load_db_tracking_items = ref(db, "users/" + auth + '/tracking_items/' + item_data.item_uid);
    const dbRef = ref(db);
    get(child(dbRef, "users/" + auth + '/tracking_items/' + item_data.item_uid)).then((productsnapcheck) => {
        console.log(productsnapcheck.val());
        if(productsnapcheck.val() === null){
            update(ref(db, 'users/' + auth + '/tracking_items'), {
                [item_data.item_uid]: {
                    // neeed to fix spelling
                    'currancy':item_data.currency,
                    'url': item_data.item_website,
                    'target_price': price_target,
                    'item_uid': item_data.item_uid,
                    'item_url': item_data.item_url
                }
            }).then(function(){
                update_user_tracking_item(auth, 'add');
            }).catch(function(err){
                console.log(err)
            });
        }else{
            console.log('already Added');
        }
    });
}


function update_tracking_item(item_uid, operator){
    const dbRef = ref(db);
    get(child(dbRef, 'p_p_data/' + item_uid + '/users_tracking_num')).then(function(snapshot) {
        var item_counter = Number(snapshot.val());
        if(operator === 'add') item_counter++;
        else item_counter--;
        update(ref(db, 'p_p_data/' + item_uid),{users_tracking_num: item_counter});
    });
}

function update_user_tracking_item(userauth, operator){
    const dbRef = ref(db);
    get(child(dbRef, 'users/' + userauth + '/num_of_t_items')).then(function(snapshot) {
        var counter = Number(snapshot.val());
        if(operator === 'add') counter++;
        else counter--;
        update(ref(db, 'users/' + userauth),{num_of_t_items: counter});
    });
}

function on_remove(userauth){
    $('.a_del_item').click(function(e){
        e.preventDefault();
        var id = $(this).parent().attr("id");
        // alert(id);
        remove_item(userauth, id);
        alert("Removed Successfully")
    });
}

function remove_item(userauth, item_id){
    remove(ref(db, 'users/' + userauth + '/tracking_items/' + item_id)).then(function(){
        console.log(item_id);    
        update_user_tracking_item(userauth, 'operator');
        update_tracking_item(item_id, 'operator');
        // });
    });
}

function on_replace() {
    $('.rep_item').click(function(e){
        e.preventDefault;
        var item_id = $(this).parent().parent().parent().attr('id');
        $('.add-item').attr("id", item_id);
    });
}

function close_pop(){
    $('#myModal').on('hidden.bs.modal', function (e) {
        e.preventDefault;
        $('.add-item').attr("id", "");
        $('#add_item_panel').css('display','');
        $('#select_dialog').css('display','none');
        $('#size-list').html('');
        $('#item-link, #price_note').val('');
        $('.add-item').removeClass('disabled');
        $('.add-item').prop('disabled', false);
    });
}

$('.signOut').click(function(e){
    e.preventDefault();
    firebase.auth().signOut().then(function() {
        // Sign-out successful.
        window.location = window.location.origin;
    }).catch(function(error) {
        // An error happened.
        alert(error.message);
    });
});




          

        // askForApproval();



        // function askForApproval() {
        //   if(Notification.permission === "granted") {
        //     createNotification('Wow! This is great', 
        //                        'created by @study.tonight', 
        //                        'https://www.studytonight.com/css/resource.v2/icons/studytonight/st-icon-dark.png');
        //   } else {
        //     Notification.requestPermission(permission => {
        //         if(permission === 'granted') {
        //             createNotification('Wow! This is great', 'created by @study.tonight', 'https://www.studytonight.com/css/resource.v2/icons/studytonight/st-icon-dark.png');
        //         }else {
        //             alert("Notifications are blocked. Please enable them in your browser."); 
        //         }
        //     });
        //   }
        // }

        // function createNotification(title, text, icon) {
        //   const noti = new Notification(title, {
        //     body: text,
        //     icon
        //   });
        // }