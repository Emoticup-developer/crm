import 'dart:nativewrappers/_internal/vm/lib/ffi_allocation_patch.dart';

import 'package:crm_ui/homepage/homepage.dart';
import 'package:crm_ui/server/server.dart';
import 'package:flutter/material.dart';

class TicketPage extends StatefulWidget {
  const TicketPage({super.key});

  @override
  State<TicketPage> createState() => _TicketPageState();
}

class _TicketPageState extends State<TicketPage> {
  final TextEditingController ticketIdController = TextEditingController();
  final TextEditingController subjectController = TextEditingController();
  final TextEditingController additionalInfoController =
      TextEditingController();
  final TextEditingController emailNotificationController =
      TextEditingController();

  final List<String> ticketTypes = ['Type 1', 'Type 2', 'Type 3'];
  final List<String> ticketSources = ['Source 1', 'Source 2', 'Source 3'];
  final List<String> ticketPriorities = ['High', 'Medium', 'Low'];
  final List<String> offices = ['Office A', 'Office B', 'Office C'];
  final List<String> machines = ['Machine X', 'Machine Y', 'Machine Z'];

  bool isadd = false;
  bool isedit = false;
  bool isview = true;

  @override
  Widget build(BuildContext context) {
    final double width = MediaQuery.of(context).size.width;
    final double height = MediaQuery.of(context).size.height;
    return Scaffold(
      appBar: AppBarForAll(context),
      drawer: DrawerForAll(),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              margin: EdgeInsets.all(8),
              width: double.infinity,
              height: height * 0.10,
              decoration: BoxDecoration(
                color: Colors.white,
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(12),
                      color: const Color.fromARGB(105, 255, 193, 7),
                    ),
                    width: width * 0.20,
                    child: ListTile(
                      onTap: () {
                        isview = true;
                        isedit = false;
                        isadd = false;
                        setState(() {});
                      },
                      leading: Icon(Icons.view_agenda_outlined),
                      title: Text("View All"),
                    ),
                  ),
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(12),
                      color: const Color.fromARGB(105, 255, 193, 7),
                    ),
                    width: width * 0.20,
                    child: ListTile(
                      onTap: () {
                        isview = false;
                        isedit = false;
                        isadd = true;
                        setState(() {});
                      },
                      leading: Icon(Icons.add_outlined),
                      title: Text("Add Ticket"),
                    ),
                  ),
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(12),
                      color: const Color.fromARGB(105, 255, 193, 7),
                    ),
                    width: width * 0.20,
                    child: ListTile(
                      onTap: () {
                        isview = false;
                        isedit = true;
                        isadd = false;
                        setState(() {});
                      },
                      leading: Icon(Icons.update_outlined),
                      title: Text("Update"),
                    ),
                  ),
                ],
              ),
            ),
            Visibility(
              visible: isadd,
              child: Center(
                child: FutureBuilder(
                    future: fetchDataDashboard("api/ticket_meta"),
                    builder: (context, snapshot) {
                      if (snapshot.connectionState == ConnectionState.waiting) {
                        return Center(child: CircularProgressIndicator());
                      } else if (snapshot.hasError) {
                        return Center(child: Text('Error: ${snapshot.error}'));
                      } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
                        return Center(child: Text('No offices available.'));
                      }

                      return Container(
                        width: width * 0.60,
                        padding: const EdgeInsets.all(16.0),
                        margin: const EdgeInsets.all(16.0),
                        color: const Color.fromARGB(255, 255, 255, 255),
                        child: SingleChildScrollView(
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Center(
                                    child: Text(
                                  "Create Ticket",
                                  textAlign: TextAlign.center,
                                  style: TextStyle(
                                      fontWeight: FontWeight.bold,
                                      fontSize: 23),
                                )),
                              ),

                              TextField(
                                controller: ticketIdController,
                                decoration: const InputDecoration(
                                  labelText: 'Ticket ID',
                                  border: OutlineInputBorder(),
                                ),
                              ),
                              const SizedBox(height: 16.0),

                              TextField(
                                controller: subjectController,
                                decoration: const InputDecoration(
                                  labelText: 'Subject',
                                  border: OutlineInputBorder(),
                                ),
                              ),
                              const SizedBox(height: 16.0),
                              Text(
                                  snapshot.data![0]["ticket_types"].toString()),
                              // Ticket Type Dropdown
// 

                              const SizedBox(height: 16.0),
                              // Ticket Source Dropdown
                              DropdownButtonFormField<String>(
                                decoration: const InputDecoration(
                                  labelText: 'Ticket Source',
                                  border: OutlineInputBorder(),
                                ),
                                items: ticketSources.map((source) {
                                  return DropdownMenuItem(
                                      value: source, child: Text(source));
                                }).toList(),
                                onChanged: (value) {},
                              ),
                              const SizedBox(height: 16.0),
                              // Priority Dropdown
                              DropdownButtonFormField<String>(
                                decoration: const InputDecoration(
                                  labelText: 'Priority',
                                  border: OutlineInputBorder(),
                                ),
                                items: ticketPriorities.map((priority) {
                                  return DropdownMenuItem(
                                      value: priority, child: Text(priority));
                                }).toList(),
                                onChanged: (value) {},
                              ),
                              const SizedBox(height: 16.0),
                              // Office Dropdown
                              DropdownButtonFormField<String>(
                                decoration: const InputDecoration(
                                  labelText: 'Office',
                                  border: OutlineInputBorder(),
                                ),
                                items: offices.map((office) {
                                  return DropdownMenuItem(
                                      value: office, child: Text(office));
                                }).toList(),
                                onChanged: (value) {},
                              ),
                              const SizedBox(height: 16.0),
                              // Machine Dropdown
                              DropdownButtonFormField<String>(
                                decoration: const InputDecoration(
                                  labelText: 'Machine',
                                  border: OutlineInputBorder(),
                                ),
                                items: machines.map((machine) {
                                  return DropdownMenuItem(
                                      value: machine, child: Text(machine));
                                }).toList(),
                                onChanged: (value) {},
                              ),
                              const SizedBox(height: 16.0),
                              // Additional Information
                              TextField(
                                controller: additionalInfoController,
                                maxLines: 3,
                                decoration: const InputDecoration(
                                  labelText: 'Additional Information',
                                  border: OutlineInputBorder(),
                                ),
                              ),
                              const SizedBox(height: 16.0),
                              // Email Notification Toggle
                              SwitchListTile(
                                title: const Text('Email/SMS Notification'),
                                value: true,
                                onChanged: (value) {},
                              ),
                              const SizedBox(height: 16.0),
                              // Submit Button
                              Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceEvenly,
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  Center(
                                    child: ElevatedButton(
                                      onPressed: () {
                                        // Handle form submission
                                      },
                                      style: ElevatedButton.styleFrom(
                                        backgroundColor: Colors.amber,
                                        padding: const EdgeInsets.symmetric(
                                            horizontal: 40.0, vertical: 15.0),
                                      ),
                                      child: const Text(
                                        'Submit',
                                        style: TextStyle(fontSize: 16.0),
                                      ),
                                    ),
                                  ),
                                  Center(
                                    child: ElevatedButton(
                                      onPressed: () {
                                        // Handle form submission
                                      },
                                      style: ElevatedButton.styleFrom(
                                        backgroundColor: Colors.grey,
                                        padding: const EdgeInsets.symmetric(
                                            horizontal: 40.0, vertical: 15.0),
                                      ),
                                      child: const Text(
                                        'Close',
                                        style: TextStyle(fontSize: 16.0),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ),
                      );
                    }),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
