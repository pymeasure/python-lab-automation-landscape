# Generated table

<table>
<!-- <colgroup>
<col width="30%" />
<col width="70%" />
</colgroup> -->
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
<th>Link</th>
<th>License</th>
<th>Activity</th>
</tr>
</thead>
<tbody>
{% for project_hash in site.data.projects -%}
{% assign project = project_hash[1] -%}
<!-- # TODO assign forge from project.repo_url
# TODO assign repoid from project.repo_url -->
<tr>

<td>{{ project.name }}</td>
<td>{{ project.description }}</td>
<td markdown="span">
[repo]({{ project.repo_url }}){% if project.docs_url %} /[docs]({{ project.docs_url }}) {% endif %}
</td>
<td markdown="span">{% if project.license %} {{ project.license }} {% endif %}</td>
<td markdown="span">
<!-- ![Last commit](https://img.shields.io/github/last-commit/ralph-group/pymeasure.svg?maxAge=300) -->
<!-- TODO: showlast commit, commits/year -->
</td>
<!-- TODO: version
![release](https://img.shields.io/github/v/release/pymeasure/pymeasure) -->
</tr>
{% endfor %}
</tbody>
</table>

# Overview table

{% include_relative converted_table.md %}

Note: The original version of the table lived at https://ethercalc.net/1anmq248ktu6
