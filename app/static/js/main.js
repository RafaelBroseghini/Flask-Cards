$('.corner')
  .popup()
;

$('.ui.dropdown')
  .dropdown()
;

function showModal(el) {
  $('.ui.long.modal', function(){
    let card = $(el).parent().parent().parent(),
    topic = card.find(".topic").text(),
    question = card.find(".question").text(),
    modaltitle = document.querySelector(".modaltitle")

    console.log(card);
    console.log(topic);
    console.log(question);

    modaltitle.textContent = topic;
    console.log(modaltitle.textContent);

    $(".highlight").remove();
    $(".modalcontent").text("").append(question)
  })
  .modal('show');
}

function showDescription(element) {
  $(element).find(".floated").toggleClass("toggle");
   
}


