const stories = [
  {% for story in stories %}
    {
      title: "{{ story.title|escapejs }}",
      location: "{{ story.location|escapejs }}",
      lat: {{ story.latitude|default:"null" }},
      lon: {{ story.longitude|default:"null" }}
    }{% if not forloop.last %},{% endif %}
  {% endfor %}
];
