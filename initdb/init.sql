-- initdb/init.sql
CREATE TYPE security_level AS ENUM ('public','internal','confidential');
CREATE TYPE urgency_level AS ENUM ('normal','urgent','immediate');
CREATE TYPE processing_status AS ENUM ('pending','in_progress','completed','archived');

CREATE TABLE document_types (
  document_type_id uuid PRIMARY KEY,
  name varchar NOT NULL UNIQUE,
  description text
);

CREATE TABLE issuing_bodies (
  issuing_body_id uuid PRIMARY KEY,
  name varchar NOT NULL UNIQUE
);

CREATE TABLE dispatches (
  dispatch_id uuid PRIMARY KEY,
  document_number varchar NOT NULL UNIQUE,
  summary text,
  page_count integer,
  security_level security_level NOT NULL,
  urgency_level urgency_level NOT NULL,
  processing_status processing_status NOT NULL,
  document_type_id uuid NOT NULL REFERENCES document_types(document_type_id),
  issuing_body_id uuid NOT NULL REFERENCES issuing_bodies(issuing_body_id),
  creator_user_id uuid NOT NULL,
  approver_user_id uuid,
  arrival_timestamp timestamp,
  effective_timestamp timestamp,
  expiration_timestamp timestamp,
  approved_at timestamp,
  created_at timestamp NOT NULL,
  updated_at timestamp NOT NULL
);

CREATE TABLE dispatch_recipients (
  dispatch_id uuid REFERENCES dispatches(dispatch_id),
  user_id uuid,
  notified_at timestamp,
  PRIMARY KEY (dispatch_id, user_id)
);

CREATE TABLE dispatch_processors (
  dispatch_id uuid REFERENCES dispatches(dispatch_id),
  user_id uuid,
  assigned_at timestamp NOT NULL,
  deadline timestamp,
  PRIMARY KEY (dispatch_id, user_id)
);

CREATE TABLE dispatch_followers (
  dispatch_id uuid REFERENCES dispatches(dispatch_id),
  user_id uuid,
  followed_at timestamp NOT NULL,
  PRIMARY KEY (dispatch_id, user_id)
);

CREATE TABLE dispatch_attachments (
  dispatch_id uuid REFERENCES dispatches(dispatch_id),
  drive_item_id uuid,
  attached_at timestamp NOT NULL,
  PRIMARY KEY (dispatch_id, drive_item_id)
);

CREATE TABLE dispatch_comments (
  comment_id uuid PRIMARY KEY,
  dispatch_id uuid NOT NULL REFERENCES dispatches(dispatch_id),
  author_user_id uuid NOT NULL,
  content text NOT NULL,
  created_at timestamp NOT NULL,
  updated_at timestamp NOT NULL
);

CREATE TABLE dispatch_views (
  view_id uuid PRIMARY KEY,
  dispatch_id uuid NOT NULL REFERENCES dispatches(dispatch_id),
  user_id uuid NOT NULL,
  viewed_at timestamp NOT NULL
);
