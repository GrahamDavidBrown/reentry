const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
const msgEndpoint = "/api/message/";
const user1 = $('#from-user').attr('value');
const user2 = $('#to-user').attr('value');
// const user1 = document.getElementsByClassName("from-user")[0].getAttribute("id");
// const user2 = document.getElementsByClassName("to-user")[0].getAttribute("id");

function sendMessage() {

  console.log("user1: ", user1);
  console.log("user2: ", user2);

    let content = $("textarea").val();
    if (content != "") {
        $.ajax({
            beforeSend: function(xhr) { xhr.setRequestHeader("X-CSRFToken", csrftoken); },
            type: "POST",
            url: msgEndpoint,
            data: JSON.stringify({
                   "sender": user1,
                   "recipient": user2,
                   "content": content,
                   "sent_at": null,
                   "read_at": null,
                  }),
            dataType: "json",
            contentType: "application/json",
            success: function() { location.reload(); },
        });

    }
    else {
        alert("I can't send an empty message");
    }
}
