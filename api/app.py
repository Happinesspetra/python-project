from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

@app.route("/")
def home():
    return render_template("index.html", 
                         name="Happiness Michael",
                         features=["Web Development", "UI/UX Design", "Python Programming", "Data Analysis"],
                         projects=[
                             {
                                 "title": "E-commerce Platform", 
                                 "description": "Full-stack e-commerce solution with React and Flask", 
                                 "tags": ["Web", "Python", "React"],
                                 "link": "https://happy-ecommerce.vercel.app/"
                             },
                             {
                                 "title": "Data Visualization Dashboard", 
                                 "description": "Interactive dashboard for business analytics", 
                                 "tags": ["Data", "Python", "JavaScript"],
                                 "link": "https://data-dashboard-example.com"
                             },
                             {
                                 "title": "Mobile App Design", 
                                 "description": "UI/UX design for fitness tracking app", 
                                 "tags": ["Design", "Figma", "Prototyping"],
                                 "link": "https://dribbble.com/happibo"
                             },
                             {
                                 "title": "Portfolio Website", 
                                 "description": "Responsive portfolio website with modern design", 
                                 "tags": ["Web", "HTML/CSS", "JavaScript"],
                                 "link": "https://happiness-portfolio.vercel.app"
                             },
                             {
                                 "title": "Task Management App", 
                                 "description": "Productivity app for managing daily tasks", 
                                 "tags": ["Web", "React", "Firebase"],
                                 "link": "https://task-app-example.com"
                             },
                             {
                                 "title": "Weather Application", 
                                 "description": "Real-time weather data visualization", 
                                 "tags": ["API", "JavaScript", "CSS"],
                                 "link": "https://weather-app-example.com"
                             }
                         ],
                         skills=["Python", "JavaScript", "HTML", "CSS", "Flask", "React", "Next.js", "Tailwind", "Typescript"],
                         about="I'm a passionate developer and designer with 3 years of experience creating digital solutions that solve real-world problems. I specialize in building beautiful, functional web applications with intuitive user interfaces."
                         )

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('../static', path)

# Required for Vercel deployment
def vercel_handler(request):
    with app.app_context():
        response = app.full_dispatch_request()
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }

if __name__ == "__main__":
    app.run(debug=True)