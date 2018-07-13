$('.corner')
  .popup()
;

$('.ui.search')
  .search({
    apiSettings: {
      url: '/cards'
    },
    fields: {
      results: 'items',
      title: 'topic'
    }
  })
;

