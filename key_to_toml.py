import toml

output_file = ".streamlit/secrets.toml"

with open("private/raspberry1-45ee2-firebase-adminsdk-5h0yc-acdceb5727.json") as json_file:
    json_text = json_file.read()

config = {"textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)