<?php
include 'config.php';

$trip_type     = $_POST['trip_type'];
$pickup        = $_POST['pickup_location'];
$dropoff       = $_POST['dropoff_location'] ?? '';
$pickup_date   = $_POST['pickup_date'];
$dropoff_date  = $_POST['dropoff_date'] ?? '';
$pickup_hour   = $_POST['pickup_hour'] ?? '';
$phone         = $_POST['phone_number'];

// Save to DB
$stmt = $conn->prepare("INSERT INTO bookings (trip_type, pickup_location, dropoff_location, pickup_date, dropoff_date, pickup_hour, phone) VALUES (?, ?, ?, ?, ?, ?, ?)");
$stmt->bind_param("sssssss", $trip_type, $pickup, $dropoff, $pickup_date, $dropoff_date, $pickup_hour, $phone);
$stmt->execute();

// Redirect to WhatsApp
$msg = "New " . ucfirst($trip_type) . " Booking%0A";
$msg .= "Pickup: $pickup%0A";
if ($dropoff) $msg .= "Dropoff: $dropoff%0A";
$msg .= "Date: $pickup_date%0A";
if ($dropoff_date) $msg .= "Return: $dropoff_date%0A";
if ($pickup_hour) $msg .= "Hour: $pickup_hour%0A";
$msg .= "Phone: $phone";

$whatsapp_number = "919560522802"; // Your WhatsApp number
header("Location: https://wa.me/$whatsapp_number?text=$msg");
exit;
?>
