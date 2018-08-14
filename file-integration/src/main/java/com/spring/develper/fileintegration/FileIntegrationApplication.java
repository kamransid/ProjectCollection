package com.spring.develper.fileintegration;

import java.io.File;


//import org.springframework.messaging.Message;
import org.springframework.integration.file.FileNameGenerator;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
//import org.springframework.integration.Message;
import org.springframework.integration.dsl.IntegrationFlowBuilder;
import org.springframework.integration.dsl.IntegrationFlows;
import org.springframework.integration.dsl.file.Files;
import org.springframework.integration.file.remote.session.SessionFactory;
import org.springframework.integration.ftp.session.DefaultFtpSessionFactory;
import org.springframework.integration.transformer.GenericTransformer;



@SpringBootApplication
public class FileIntegrationApplication {
	
	
	
	@Bean
	DefaultFtpSessionFactory ftpSessionFactory() {
		DefaultFtpSessionFactory ftpSessionFactory = new DefaultFtpSessionFactory();
		ftpSessionFactory.setPort(21);
		return ftpSessionFactory;
	}
	
	
	
	
	@Bean
	IntegrationFlowBuilder file(@Value("${input-directory:${HOME}/Desktop/in}") File in, DefaultFtpSessionFactory ftpSessionfactory) {
		
		return IntegrationFlows.from(Files.inboundAdapter(in).autoCreateDirectory(true).preventDuplicates())
				.transform(File.class, (GenericTransformer<File,String>) (File source)->{
					return  null;
				}).handleWithAdapter(adapter->
				adapter.ftp(ftpSessionfactory)
				.fileNameGenerator(new FileNameGenerator() {

					@Override
					public String generateFileName(Message<?> message) {
						// TODO Auto-generated method stub
						
						return null;
					}
				})
						
						
						);
		
	} 
	
	

	public static void main(String[] args) {
		SpringApplication.run(FileIntegrationApplication.class, args);
	}
}
