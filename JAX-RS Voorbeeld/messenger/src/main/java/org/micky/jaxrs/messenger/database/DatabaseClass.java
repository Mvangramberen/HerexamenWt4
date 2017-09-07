package org.micky.jaxrs.messenger.database;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import org.micky.jaxrs.messenger.model.Message;
import org.micky.jaxrs.messenger.model.Movie;
import org.micky.jaxrs.messenger.model.Profile;

import redis.clients.jedis.*;


public class DatabaseClass {
	
	// Redis connectie voor jax-rs
	private static Jedis redisConnectie = new Jedis();
	
	private static ArrayList<Movie> movies = new ArrayList<>();
	
	
	
	public static ArrayList<Movie> getMovies(){ return movies;}
	public static void setMovie(Movie movie) {movies.add(movie); }
	

}
