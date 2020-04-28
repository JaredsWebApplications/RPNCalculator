const API_URL= '/api'

function insert(ch) {
    s = document.form.field.value
    if (s.length > 0) {
        document.form.field.value = s + " " + ch
    }
    else {
        document.form.field.value = ch
    }
}
function enter(){
  //var message = $("#stringexpression").val();
  //console.log(message);
  alert("before post request")
  $.post({
    url: "https://localhost:5000/api/",
    data: JSON.stringify({"message": "Hello"}),
  });
  //$.ajax({
      //url: "https://localhost:5000/api/",
      //type: "POST",
      //contentType: "application/json",
      //data: JSON.stringify({"message": "Hello"}),
      //dataType: "json"
  //}).done(function(data) {
      //console.log(data);
  //});
  alert("post sent")
}
function allClear() {
    document.form.field.value = ""
    }

function del() {
    var s = document.form.field.value
    n = s.length
    if (n > 1) {
        document.form.field.value = s.slice(0, n-2);    
    }
    else {
        allClear();
    }
}
