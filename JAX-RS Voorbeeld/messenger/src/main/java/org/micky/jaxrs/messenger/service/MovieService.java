package org.micky.jaxrs.messenger.service;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

import org.micky.jaxrs.messenger.database.DatabaseClass;
import org.micky.jaxrs.messenger.model.Movie;

public class MovieService {

	private ArrayList<Movie> films = DatabaseClass.getMovies();

	public MovieService() throws IOException {
		
		String sURL = "http://www.omdbapi.com/?t=deadpool&apikey=plzBanMe";

	    
	    URL url = new URL(sURL);
	    HttpURLConnection request = (HttpURLConnection) url.openConnection();
	    request.connect();
	    
	   Movie film = new Movie("deadpool", request.toString());
	    
		this.films = films.add(film);
	}
	
	
}
