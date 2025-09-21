import PySimpleGUI as sg
import pandas as pd

class MovieApp:
    def __init__(self):
        
        try:
            self.movies_df = pd.read_csv('movies.csv')
        except FileNotFoundError:
            sg.popup_error("Error: movies.csv not found!")
            exit()
        
        Layout = [
            [sg.Text('Movie Dataset Explorer', font=('Helvetica', 18))],
            [sg.Text('Enter a Genre', size=(15,1)), sg.InputText(key='-INPUT-')],
            [sg.Button('Search')],
            [sg.Text('Results: ')],
            [sg.Multiline(size=(60,15), disabled=True, key='-OUTPUT')]
        ]

        self.window = sg.Window('Movie Explorer', Layout)

    def search_movies(self, genre_query):
        results_df = self.movies_df[self.movies_df['genres'].str.contains(genre_query, case=False, na=False)]
        return results_df
    
    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Search':
                search_term = values['-INPUT-']
                search_results = self.search_movies(search_term)
               
                if not search_results.empty:
                    display_text = search_results['title'].to_string(index=False)
                else:
                    display_text = f'No movies found for the genre: "{search_term}"'
                
                self.window['-OUTPUT'].update(display_text)
               
        self.window.close()

if __name__ == "__main__":
    app = MovieApp()
    app.run()