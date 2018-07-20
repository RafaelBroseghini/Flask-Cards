$('.corner')
  .popup()
;

function showModal(el) {
  $('.ui.long.modal', function(){
    let card = $(el).parent().parent(),
    topic = card.find(".topic").text(),
    question = card.find(".question").text(),
    modaltitle = document.querySelector(".modaltitle")

    modaltitle.textContent = topic;

    $(".highlight").remove();
    $(".modalcontent").append(question)
  })
  .modal('show');
}


