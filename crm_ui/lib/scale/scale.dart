import 'package:flutter/material.dart';

getWidget(BuildContext context, double size) {
  return MediaQuery.of(context).size.width * size;
}

getHeight(BuildContext context, double size) {
  return MediaQuery.of(context).size.height * size;
}
