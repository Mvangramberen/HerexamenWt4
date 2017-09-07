package org.micky.jaxrs.messenger.model;



public class Movie {
	private String titel;
	private String json;

	public Movie(String titel, String json) {
		super();
		this.titel = titel;
		this.json = json;
	}

	
	public String getJson() {
		return json;
	}


	public void setJson(String json) {
		this.json = json;
	}


	public String getTitel() {
		return titel;
	}

	public void setTitel(String titel) {
		this.titel = titel;
	}

	@Override
	public String toString() {
		return "Movie [titel=" + titel + "]";
	}
	
	

}
