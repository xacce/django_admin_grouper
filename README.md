## Django admin groupert
![alt=""](http://www.webpagescreenshot.info/i/381676-27201331833pm.png)

#Install:
1. Copy ```django_admin_grouper``` folder in you project root directory

2. In settings.py
```
INSTALLED_APPS = (
  #...
  'django_admin_grouper',
  #...
  )
```
```
TEMPLATE_DIRS = (
  #...
  '/project_root_directory/django_admin_grouper/templates/',
  #...
    )
```

## If you use custom admin templates (```change_list_results.html```)
Modify and use this code:
```
 {% if cl.model_admin.regroup_by %}
                {# django-admin-grouper-part st #}
                {% admin_regroup_by cl.result_list results cl.model_admin.regroup_by as new_list %}
                {% for item,value in new_list.items %}
                    <tr>
                        <td colspan="{{ value.0|length }}"><h4>{{ item }}</h4></td>
                    </tr>
                    {% for result in value %}
                        <tr class="{% cycle 'row1' 'row2' %}">{% for item in result %}{{ item }}{% endfor %}</tr>
                    {% endfor %}
                {% endfor %}
                {# django-admin-grouper-part end #}
            {% else %}
                {% for result in results %}
                    {% if result.form.non_field_errors %}
                        <tr>
                            <td colspan="{{ result|length }}">{{ result.form.non_field_errors }}</td>
                        </tr>
                    {% endif %}
                    <tr class="{% cycle 'row1' 'row2' %}">{% for item in result %}{{ item }}{% endfor %}</tr>
                {% endfor %}
            {% endif %}
```
