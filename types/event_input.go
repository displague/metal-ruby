// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// EventInput event input
//
// swagger:model EventInput
type EventInput struct {

	// body
	Body string `json:"body,omitempty"`

	// private
	Private bool `json:"private,omitempty"`

	// state
	State string `json:"state,omitempty"`

	// type
	Type string `json:"type,omitempty"`
}

// Validate validates this event input
func (m *EventInput) Validate(formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *EventInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *EventInput) UnmarshalBinary(b []byte) error {
	var res EventInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
