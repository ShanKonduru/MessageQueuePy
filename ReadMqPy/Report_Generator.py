from jinja2 import Template

class ReportGenerator:
    def __init__(self, results):
        self.results = results

    def generate_html(self, output_path):
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Messaging Queue Smoke Test Report</title>
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                table, th, td {
                    border: 1px solid black;
                }
                th, td {
                    padding: 10px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
                .status-up {
                    background-color: #d4edda;
                    color: #155724;
                }
                .status-down {
                    background-color: #f8d7da;
                    color: #721c24;
                }
            </style>
        </head>
        <body>
            <h1>Messaging Queue Smoke Test Report</h1>
            <table>
                <tr>
                    <th>Queue Name</th>
                    <th>Queue URL</th>
                    <th>Queue Type</th>
                    <th>Status</th>
                </tr>
                {% for name, url, type, status in results %}
                <tr>
                    <td>{{ name }}</td>
                    <td>{{ url }}</td>
                    <td>{{ type }}</td>
                    <td class="status-{{ 'up' if status else 'down' }}">{{ 'Up' if status else 'Down' }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
        </html>
        """
        template = Template(html_template)
        html_report = template.render(results=self.results)

        with open(output_path, 'w') as f:
            f.write(html_report)