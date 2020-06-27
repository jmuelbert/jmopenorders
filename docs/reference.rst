{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}
Reference
=========

.. contents::
    :local:
    :backlinks: none


{{ heading(jmopenorders + ".__main__") }}

.. automodule:: jmopenorders.__main__
   :members:
