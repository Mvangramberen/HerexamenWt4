package org.micky.jaxrs.messenger.resources;

import javax.ws.rs.Path;
import javax.ws.rs.PathParam;

import org.micky.jaxrs.messenger.service.MovieService;

@Path("/Movie")
public class MovieResource {
	MovieService movieService = new MovieService();
	
	@Path("/{messageId}")
	public Message getMovie(@PathParam("titel" String titel) long messageId){
		return movieService.getMovie(titel);
	}
 

}
