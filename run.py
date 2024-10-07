def run_model(s, w, i):
    # Import necessary modules
    from app.services.example_service import main
    # Call the analyze_sentence function
    result, analysis = main(s, w, i)

 
    return result, analysis

if __name__ == "__main__":
    run_model()

