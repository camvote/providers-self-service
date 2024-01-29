# WIP PROJECT

This is a work-in-progress, barebones implementation of a 'self-service' site for providers using camvote.org.

It doesn't have to be pretty, it doesn't have to be complex, it should just be better than emailing the sysadmins and waiting up to a week for us to reply.

## To-Do
- [ ] Clone and convert YAML provider files to JSON [yes, back to JSON we go] 
- [ ] Add parsing of a given providers file to the template
- [ ] add dummy authentication
- [ ] if a crsid passes authentication for a given provider, allow them to:
- [ ] view the update form and send an updated list to the server
- [ ] re-authenticate user and then make changes to the provider's JSON file
- [ ] kick the user out after changes made, so that they have to reauthenticate; admins who remove themselves shouldn't be able to edit
- [ ] Create index page of all providers, logos, and whether the user is permitted to access them (like camvote at the moment)
- [ ] Add Raven authentication
- [ ] determine whether other fields (in particular logos?) to be updated?

## License
This project is licensed under GPLv3.
