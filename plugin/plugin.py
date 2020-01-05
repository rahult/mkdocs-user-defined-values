from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class UserDefinedValues(BasePlugin):

    config_scheme = (
        ('keywords', config_options.Type(list)),
        ('input-placeholder', config_options.Type(mkdocs_utils.string_types, default='{{{user-defined_values}}}'))
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_post_page(self, output_content, page, config):
        data_tag = 'data-bind-user-defined-values'
        input_boxes = ''

        # Wrap keyword with span and data tag
        for keyword in self.config['keywords']:
            output_content = output_content.replace(keyword, f'<span {data_tag}="{keyword}">{keyword}</span>')

        # Embed binding javascript
        input_boxes = '''
        <style>
            label.user-defined-values {
                width: 30%
            }

            input.user-defined-values[type=text] {
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 1px solid black;
                display: inline-block;
            }
        </style>
        '''

        for keyword in self.config['keywords']:
            javascript_variable_name = keyword.lower().replace("-", "_")
            input_boxes += f'''
                <label class="user-defined-values" for="{keyword}">{keyword}</label>
                <input class="user-defined-values" type="text" id="{keyword}" />
                <script>
                    const {javascript_variable_name} = document.getElementById('{keyword}');
                    {javascript_variable_name}.oninput = function(e) {{
                        const value = e.target.value;
                        document.querySelectorAll('[{data_tag}="{keyword}"]').forEach(function(element, _) {{
                            if (value == '') {{
                                element.innerHTML = '{keyword}';
                            }} else {{
                                element.innerHTML = value;
                            }}
                        }});
                    }};
                </script>
            '''

        output_content = output_content.replace(self.config['input-placeholder'], input_boxes)

        return output_content